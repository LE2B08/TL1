#include <cstdio>
#include <cstdlib>

int main(int argc, char* argv[])
{
	// argc�̐������J��Ԃ�
	for (int i = 0; i < argc; i++)
	{
		// ������argv��i�Ԗڂ�\��
		printf(argv[i]);

		// ���s
		printf("\n");
	}

	// �E�B���h�E�����Ȃ��悤�ɂ���
	system("pause");
	return 0;
}