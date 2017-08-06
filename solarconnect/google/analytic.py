import httplib2
import pandas as pd
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']


class GoogleAnalytics(object):
    """
    A connector to obtain data from Google Analytic
    """
    def __init__(self, account_email, key_path):
        """
        Initializes an analyticsreporting service object.

        Returns:
        analytics an authorized analyticsreporting service object.
        """

        credentials = ServiceAccountCredentials\
            .from_p12_keyfile(account_email, key_path, scopes=SCOPES)
        http = credentials.authorize(httplib2.Http())
        # Build the service object.
        analytics = build('analytics', 'v4', http=http,
                          discoveryServiceUrl=DISCOVERY_URI)
        self.analytics = analytics
        self.dataframe = None
        self.report = None

    def get_response(self, **kwargs):
        reports = []
        while True:
            response = self.analytics.reports().batchGet(**kwargs).execute()
            reports.extend(response.get('reports', []))
            next_page_token = [report.get('nextPageToken')
                for report in response.get('reports', [])]
            report_requests = kwargs.get('body').get('reportRequests', [])
            for page_token, report_request in zip(next_page_token, report_requests):
                report_request.update({"pageToken":page_token})
            if page_token == None:
                break
        self.report = {'reports': reports}
        return self

    def get_report(self):
        return self.report

    def to_pandas(self, response=None):
        """
        Parses and converts the Analytics Reporting API V4 into Pandas dataframe
        """
        if not response:
            response = self.report
        result = []
        for report in response.get('reports', []):
            columnHeader = report.get('columnHeader', {})
            dimensionHeaders = columnHeader.get('dimensions', [])
            metricHeaders = columnHeader.get(
                'metricHeader', {}).get('metricHeaderEntries', [])
            rows = report.get('data', {}).get('rows', [])

            for row in rows:
                dimensions = row.get('dimensions', [])
                dateRangeValues = row.get('metrics', [])

                dataframe = dict([(header, dimension)
                                  for header, dimension in zip(dimensionHeaders, dimensions)])

                dataframe.update(dict([(metricHeader.get('name'), value) for values in dateRangeValues
                                       for metricHeader, value in zip(metricHeaders, values.get('values'))]))

                result.append(dataframe)
        self.dataframe = pd.DataFrame(result)
        return self.dataframe

