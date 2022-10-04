from sync.SyncSeriesCommand import SyncSeriesCommand
from client.GuyaClient import GuyaClient
from model.Chapter import Chapter
from logic.SeriesLogic import SeriesLogic

if __name__ == "__main__":
    # initalise logics
    client = GuyaClient()
    series_logic = SeriesLogic()
    # get the data for the series
    kaguya_sama_series_data = client.get_kaguya_sama_series()
    kaguya_sama_series = series_logic.create_series(kaguya_sama_series_data)

    print('Beginning sync')
    SyncSeriesCommand().execute(kaguya_sama_series)
    print('Sync done!')
    input('Press enter to exit')