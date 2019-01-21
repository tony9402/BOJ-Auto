BOJ-Auto
==========
[![](https://d2gd6pc034wcta.cloudfront.net/images/logo.png)](https://www.acmicpc.net)
----------
'BOJ_AUTO'는 [Baekjoon Online Judge](https://www.acmicpc.net)의 다양한 알고리즘 문제를 풀어서 원격으로 소스를 제출하고 제출한 소스로 정답을 맞추면 [Github](https://github.com)에 Source Code를 Push합니다. 이 소스는 'Python 3'을 기반으로 만들어졌습니다.

이 프로젝트를 제작하기 전에 [ISKU](https://github.com/ISKU/BOJ-AutoCommit)님이 만드신 'BOJ-AutoCommit'와 [sjy366](https://github.com/sjy366/BOJ-Auto-Submit)님이 만드신 'BOJ-Auto-Submit'의 소스를 참고하여 제작을 하였습니다. 

Installation
----------
```
$ git clone https://github.com/tony9402/BOJ-Auto
```

**Dependency**
```
$ pip3 install requests
$ pip3 install bs4
```
- [Git](https://git-scm.com/)

How to use
----------
- 다음과 같이 Tool을 실행하여, 올바른 정보를 입력합니다.
```
$ python3 main.py (소스파일) (문제번호)
```

- Tool 실행시 다음과 같이 BOJ의 회원 정보와 GitHub의 회원 정보 및 Repository 이름을 입력하여야 합니다.

| **Input**            | **Description**
|:---------------------|:-------------------------------------------------
| **BOJ id**           | BOJ에서 사용하는 ID를 입력합니다.
| **BOJ password**     | 로그인을 위해 BOJ의 비밀번호를 입력합니다.
| **GitHub id**        | GitHub에서 사용하는 ID를 입력합니다.
| **Repository**       | Source Code를 Push할 원격저장소의 Repository의 이름을 입력합니다.

Default
----------
- 문제번호에서 가장 끝 두 자리를 00으로 바꿔 Directory를 생성한 후, 하위에 문제번호 제목으로 Source Code 파일이 저장됩니다.
- Commit Message는 항상 **"문제번호"** 입니다. (추후에 option 기능으로 추가할 예정)
- 같은 소스로 이 Tool을 이용하여 여러번 맞을 경우 맨 처음에 github에 올라간 소스만 적용됩니다.
- 같은 문제이지만 다른 소스로 이 Tool을 이용하여 맞은 경우는 최신 소스로 바뀌어서 github에 push 됩니다.

Extension
----------
- Tool을 확장하여 자유롭게 자신의 원격저장소를 관리할 수 있습니다.
- option.json에 다음 예제와 같이 원하는 Option을 설정하세요.
- (추후에 option 내용 추가 예정)

``` json
{	
	"source_path": "(Directory)\\"
}
```
> :bulb: 사용하지 않는 Option은 반드시 지워야 합니다.

> :bulb: source_path를 사용하는 경우 마지막에 \\\\을 넣어줘야 합니다.

| **Key**            | **Description**
|:-------------------|:-------------------------------------------------
| **source_path** | 제출할 소스 파일의 위치를 지정합니다.


소스파일은 하나만 만들고 그거를 가지고 제출할 문제 번호만 입력하면 그 문제번호에 맞춰 정리되니 소스파일은 하나만 생성하면 됩니다.

