
import pandas as pd

class get_item():
    def __init__(self):
        # 코스피(대기업) 종목 모두 출력
        self.get_item_kospi()
        print("코스피 종목 수: ", len(self.code_df_kospi))
        print(self.code_df_kospi)
        print(type(self.code_df_kospi))

        # 코스닥(중견기업) 종목 모두 출력
        self.get_item_kosdaq()
        print("코스닥 종목 수: ", len(self.code_df_kosdaq))
        print(self.code_df_kosdaq)


    def get_item_kospi(self):
        print("get_item_kospi!!")
        self.code_df_kospi = \
        pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=stockMkt',
                     header=0)[
            0]  # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌

        # 6자리 만들고 앞에 0을 붙인다.
        self.code_df_kospi.종목코드 = self.code_df_kospi.종목코드.map('{:06d}'.format)

        # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다.
        self.code_df_kospi = self.code_df_kospi[['회사명', '종목코드']]

        # 한글로된 컬럼명을 영어로 바꿔준다.
        self.code_df_kospi = self.code_df_kospi.rename(columns={'회사명': 'code_name', '종목코드': 'code'})
        return self.code_df_kospi

    def get_item_kosdaq(self):
        print("get_item_kosdaq!!")
        self.code_df_kosdaq = \
        pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=kosdaqMkt',
                     header=0)[
            0]  # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌

        # 6자리 만들고 앞에 0을 붙인다.
        self.code_df_kosdaq.종목코드 = self.code_df_kosdaq.종목코드.map('{:06d}'.format)

        # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다.
        self.code_df_kosdaq = self.code_df_kosdaq[['회사명', '종목코드']]

        # 한글로된 컬럼명을 영어로 바꿔준다.
        self.code_df_kosdaq = self.code_df_kosdaq.rename(columns={'회사명': 'code_name', '종목코드': 'code'})
        return self.code_df_kosdaq



if __name__ == "__main__":
    get_item()


