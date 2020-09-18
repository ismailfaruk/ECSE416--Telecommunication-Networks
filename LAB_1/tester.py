import json
import client as cl
import os

#----------------------------------------Tester Default Definitions-------------------------------
TEST_CONFIG = "TEST_CONFIG.json"
ITERATION = 100
#-------------------------------------------------------------------------------------------------

# default test config
def defaultTest():
    TestConfig = {
            "IMAGE":{
                "host":"localhost",
                "port":"1337",
                "file":"pic.jpg"
            },
            "TEXT":{
                "host":"localhost",
                "port":"1337",
                "file":"test.txt",
            }
        }
    return TestConfig

# tester runs client for n interations with given config
def tester(config):
    # running interation of client to check for errors
    host = config["host"]
    port = int(config["port"])
    filename = config["file"]
    if "iteration" in config:
        iteration = int(config["iteration"])
    else:
        iteration = ITERATION
    
    for i in range(iteration):
        try:
            cl.client(host, port, filename)
    
        except Exception as error_message:
            log.write(f"- Iteration: {i} - ERROR: {error_message}\n")

if __name__ == "__main__":
    if os.path.isfile(TEST_CONFIG):
        with open(TEST_CONFIG, "r") as configFile:
            allConfig = json.load(configFile)
    else:
        # creates test config from default tests
        allConfig = defaultTest()
        with open(TEST_CONFIG, "w") as configFile:
            json.dump(allConfig, configFile, indent = 4)

    for config in allConfig:
        logfile = f"TEST_LOG_{config}.txt"
        with open(logfile, "a") as log:
            tester(allConfig[config])