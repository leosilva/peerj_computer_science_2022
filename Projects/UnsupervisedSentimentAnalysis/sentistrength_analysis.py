import os
import subprocess
import utils as ut


def perform_sentistrength_analysis(text):
    text = text.replace("'", "''")
    result = subprocess.getoutput("java -jar sentistrenth/SentiStrengthCom.jar sentidata sentistrenth/portuguese_language/ text '{}'".format(text))
    result = result.split(" ")
    result = eval(result[0] + result[1])
    return result