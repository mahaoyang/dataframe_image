import pytest
import pandas as pd
import dataframe_image

# df = pd.read_csv('test/notebooks/data/covid19.csv', parse_dates=['date'], index_col='date')
df = pd.read_csv('covid19.csv', parse_dates=['date'], index_col='date')


class TestImage:

    def test_df(self):
        # df.tail(10).dfi.export('test/test_output/covid19.png')
        df.tail(10).dfi.export('test_output/covid19.png')

    def test_styled(self):
        # df.tail(10).style.background_gradient().export_png('test/test_output/covid19_styled.png')
        df.tail(10).style.background_gradient().export_png('test/test_output/covid19_styled.png')

    def test_mpl(self):
        # df.tail(10).dfi.export('test/test_output/covid19_mpl.png', table_conversion='matplotlib')
        df.tail(10).dfi.export('test_output/covid19_mpl.png', table_conversion='matplotlib')


if __name__ == '__main__':
    test = TestImage()
    test.test_df()
    test.test_styled()
    test.test_mpl()
