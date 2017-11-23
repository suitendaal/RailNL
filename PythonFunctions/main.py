import algoritm
import csv
import helpers

def main():

    # Files with stations and connections.
    stationsCsvFile = 'csvFiles/StationsHolland.csv'
    connectiesCsvFile = 'csvFiles/ConnectiesHolland.csv'

    # Load the stations and connections in a graph.
    critical_stations, critical_connections, graph, stationnames = helpers.load_data(stationsCsvFile, connectiesCsvFile)
    paths = helpers.add_paths(graph, stationnames)
    # best150paths, best150scores = helpers.ScorePaths(paths,critical_connections, 20)
    # algoritm.algoritm1(paths, critical_connections)

    # print(best150paths)

    algoritm.algoritm3(paths, critical_connections, stationnames)

    # routes = []
    # for stationname in stationnames:
    # route, time = algoritm.Dijkstra(graph, stationnames[4], critical_connections)
    # print([route, time])
        # routes.append([route, time])
    # print(routes)




if __name__ == "__main__":
    main()