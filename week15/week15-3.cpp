int equalSubstring(char* s, char* t, int maxCost) {
    int ans = 0;

    int N = strlen(s); //�����D�r�ꪺ����
    for(int i=0;i<N;i++){   // �r�ꪺ�j��
        printf("%c %c\n", s[i],t[i] ); //�r�ꪺ�}�C
    }
    return ans; // �Ұ�@�~1, ���H�K����0����(���׷�M����)
}
