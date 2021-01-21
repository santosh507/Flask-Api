import requests
import json
import traceback
import logging
from requests.auth import HTTPBasicAuth


class Mitigation:
    HOSTNAME = "devscapi.cloudapps.cisco.com"
    HOST_URL = "http://devscapi.cloudapps.cisco.com/"
    DEVSC_HEADERS = {
        "Host": HOSTNAME,
        "Connection": "keep-alive",
        "Origin": HOST_URL,
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    }
    PENDING_MITIGATION_ASSEMBLIES_URL = "https://devscapi.cloudapps.cisco.com/devscapp/analysis/pendingrolledmitigation"
    GENERATE_MITIGATION_ASSEMBLIES_URL = "https://devscapi.cloudapps.cisco.com/devscapp/analysis/generaterolledmitigation?assembly={}"
    # TODO: hardcoded passwords for API, need to be changed asap
    API_AUTH_DICT = {"user_name": "devscapi.gen", "password": "Dev$c83120"}
    logger = logging.Logger("Mitigation")

    def __init__(self):
        self.auth = HTTPBasicAuth(self.API_AUTH_DICT["user_name"], self.API_AUTH_DICT["password"])
        stream_format = logging.Formatter("Devsc API: [%(levelname)s] [%(asctime)s] %(message)s",
                                          datefmt="%A %d-%b-%Y %I:%M:%S %p")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_format)
        stream_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(stream_handler)

    def get_pending_mitigation_assemblies(self):
        response = requests.get(self.PENDING_MITIGATION_ASSEMBLIES_URL, headers=self.DEVSC_HEADERS, auth=self.auth)
        if not (response.ok):
            msg = "An error occurred while trying to fetch the assemblies 'status_code': {}, 'reason': {}".format(
                response.status_code, response.reason)
            self.logger.error(msg)
            self.logger.error(msg)
            return []
        assembly_list = json.loads(response.content)
        self.logger.info("Fetched assemblies {}".format(assembly_list))
        return assembly_list

    def generate_rolled_mitigation(self):
        assembly_list = self.get_pending_mitigation_assemblies()
        for assembly in assembly_list:
            try:
                url = self.GENERATE_MITIGATION_ASSEMBLIES_URL.format(assembly)
                response = requests.get(url, headers=self.DEVSC_HEADERS, auth=self.auth)
                if not (response.ok):
                    self.logger.error("An error occurred while trying to fetch the assemblies")

                if (response.ok):
                    self.logger.info("Sucessfully updated rolled mititgation status for '{}' " + url)
                    resp_dict = json.loads(response.content)
                    # self.logger.error(resp_dict)
                    self.logger.debug(resp_dict)

            # an exception raised when there is a network problem upon contacting the API
            except requests.exceptions.ConnectionError as e:
                self.logger.error("A ConnectionError exception occurred for: " + url)
                self.logger.error("There was an error connecting (ConnectionError exception):" + str(e))
                traceback.print_exc()

            # an exception raised when the API call takes too long and times out
            except requests.exceptions.Timeout as e:
                self.logger.error("A Timeout exception occurred for: " + url)
                self.logger.error("The request took too long (Timeout exception):" + str(e))
                traceback.print_exc()
                # if a timeout occurs while one of the assemblies are being mitigated,
                # continue processing the rest of the jobs but log this exception for later reference

            # generalized exception raised by 'Requests' (the API call)
            except requests.exceptions.RequestException as e:
                self.logger.error("A RequestException exception occurred for: " + url)
                self.logger.error("Failed to process due to a RequestException exception:" + str(e))
                traceback.print_exc()

            except Exception as e:
                self.logger.error("An exception occurred for: " + url)
                self.logger.error("An error has occurred:" + str(e))
                traceback.print_exc()
                self.logger.error("Exception occurred", exc_info=True)


if __name__ == '__main__':
    mitigate_obj = Mitigation()
    mitigate_obj.generate_rolled_mitigation()
