import algoritm
import csv
import helpers
import score

def main():

    # Files with stations and connections.
    stationsCsvFile = 'StationsHolland.csv'
    connectiesCsvFile = 'ConnectiesHolland.csv'

    # Load the stations and connections in a graph.
    critical_stations, critical_connections, graph, stationnames = helpers.load_data(stationsCsvFile, connectiesCsvFile)
    paths = helpers.add_paths(graph, stationnames)
    best150paths, best150scores = helpers.ScorePaths(paths,critical_connections, 20)
    #algoritm.algoritm1(paths, critical_connections)

    print(best150paths)




if __name__ == "__main__":
    main()