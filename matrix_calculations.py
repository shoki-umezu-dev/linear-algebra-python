# ベクトルの足し算関数
def vector_sum(A, B):
    # for文による繰り返しの抽出とs = A[i] + B[i]の出力結果の受け皿として空のリストを準備
    result = []
    # iをAの要素の数の範囲で繰り返し抽出する
    # for文は回数と添え字を決めており、Aに限定している訳ではない
    # 何かしらのリストのi番目の要素を要素の数だけ繰り返し抽出するという意味
    for i in range(len(A)):
        s = A[i] + B[i]
        # appendを使ってresultリストにsを追加
        result.append(s)
    return result
vec_a = [15, 18, 21, 40]
vec_b = [-3, -4, 0, 50]
print(vector_sum(vec_a, vec_b))

# 行列の足し算関数
def mat_sum(A, B):
    # 足し算の最終結果を入れる空のリストを用意する
    result = []
    # まず、行の数分だけ繰り返すfor文を作成する
    for i in range(len(A)):
        # 列のfor文に対する空のリストを用意する
        row = [] 
        # 行数に対する列の数分だけ繰り返すfor文を作成する
        for j in range(len(A[i])):
            #繰り返し抽出されたi行とj列の足し算を行う
            s = A[i][j] + B[i][j]
            # sをrowに追加、列の要素が集まって1行分が完成
            row.append(s)
            # rowをresultに追加、1行分、2行分と足されていって行列が完成
        result.append(row)
    return result
matrix_a = [[4, 5],[2,11]]
matrix_b = [[1.5, 2.3], [-0.7, 3.6]]
print(mat_sum(matrix_a, matrix_b))