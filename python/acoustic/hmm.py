def main():
    M = [[[0.6, 0.4, 0.6, 0.4], [0.5, 0.5, 0.7, 0.3], [0.8, 0.2, 0.5, 0.5]], [[0.3, 0.7, 0.2, 0.8], [0.4, 0.6, 0.6, 0.4], [0.8, 0.2, 0.5, 0.5]]]
    print('M=["Rの確率","Bの確率","とどまる確率","移動する確率"]\n')
    print("M1=[\n[0.6,0.4,0.6,0.4],\n[0.5,0.5,0.7,0.3],\n[0.8,0.2,0.5,0.5]\n],\nM2=[\n[0.6,0.4,0.6,0.4],\n[0.5,0.5,0.7,0.3],\n[0.8,0.2,0.5,0.5]\n]")
    x = input("RとBの文字列を入力してください: ")
    n = len(x)
    k=len(M[0])
    list=[]
    for i in range(1, n - k + 1):
        for j in range(1,n-i-k+2):
            list.append([i,j,n-i-j])
    import numpy as np
    import functools
    import operator
    mp = []
    for m_num in range(len(M)):
        common = M[m_num][0][3] * M[m_num][1][3] * M[m_num][2][3]
        p = []
        for i in range(len(list)):
            f_break=list[i][0]
            s_break=f_break+list[i][1]
            t_break=s_break+list[i][2]

            area1=x[0:f_break]
            area2=x[f_break:s_break]
            area3=x[s_break:t_break]

            p_area1=(M[m_num][0][0]**(area1.count('R')))*(M[m_num][0][1]**(area1.count('B')))*(M[m_num][0][2]**(len(area1)-1))
            p_area2=(M[m_num][1][0]**(area2.count('R')))*(M[m_num][1][1]**(area2.count('B')))*(M[m_num][1][2]**(len(area2)-1))
            p_area3=(M[m_num][2][0]**(area3.count('R')))*(M[m_num][2][1]**(area3.count('B')))*(M[m_num][2][2]**(len(area3)-1))

            p.append(np.prod([p_area1,p_area2,p_area3])*common)        
        mp.append(sum(p))
    print('["M1の確率","M2の確率"]=' + str(mp))
    print("もっとも"+str(x)+"が出る確率が高いのは,M"+ str(np.argmax(mp)+1)+"です。")

if __name__ == "__main__":
    main()
