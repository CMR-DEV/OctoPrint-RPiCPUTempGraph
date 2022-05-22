def callback(comm, parsed_temps):

    # Reading /sys/class/thermal/thermal_zone0/temp may be the best method for obtaining Pi CPU temps since spawning "vcgencmd measure_temp" is significantly slower ( ~56% )
    
    tempPath    = "/sys/class/thermal/thermal_zone0/temp"   # Make customizable in settings? Multiple temp sensors?    
    
    tempLines   = open( tempPath, "r" ).read().splitlines() # ToDo: Error handling by custom logger
    tempRaw     = int( tempLines[0] )
    temp        = round( tempRaw / 1000, 1 )                # 20°C equals 20000
    
    # tempID = ( actualTemp, targetTemp ) see https://docs.octoprint.org/en/master/plugins/hooks.html#octoprint-comm-protocol-temperatures-received
    parsed_temps.update( RPiCPU = ( temp, None ) ) 
    
    return parsed_temps

################################################################################

__plugin_name__         = "Raspberry Pi CPU Temperature Graph"
__plugin_description__  = "Adds the Raspberry Pi's CPU temperature to Plotly Temp Graph by jneilliii"
__plugin_author__       = "CMR-DEV"
__plugin_url__          = "https://github.com/CMR-DEV/OctoPrint-RPiCPUTempGraph"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_version__      = "1.0.0"
__plugin_hooks__        = {
    "octoprint.comm.protocol.temperatures.received": ( callback, 1 )
}