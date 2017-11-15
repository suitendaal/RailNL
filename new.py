import csv
import helpers

def main():

    critical_stations, critical_connections, graph, stationnames = helpers.load_data()

    paths = helpers.add_paths(graph, stationnames)

    best150paths, best150scores = helpers.ScorePaths(paths, critical_connections)

if __name__ == "__main__":
    main()