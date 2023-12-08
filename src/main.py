from feat_engg import feat_engg
from data_pull import data_pull


def main() -> None:
    df = data_pull.run_seq()
    df = feat_engg.run_seq(df)
    print(df)


if __name__ == "__main__":
    main()
