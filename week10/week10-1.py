N = int(input('�п�JN:'))
#�H�e�O�� for�j��g, ���ѥ� �禡�I�s�禡�Ӽg
def func(n):
  if n==1: return 1 # �פ����, �� �ƾ��k�ǪkN=1����
  return n * func(n-1) # �禡�I�s�禡, ��j���D, �令�h�� �p���D
ans = func(N)
print(ans)
