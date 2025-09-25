import sys
import io

s = input()
st = []

for ch in s:
    if ch in '[(':
        st.append(ch)

    else:

        if not st:
            print("0")
            sys.exit(0)

        if ch == ')':
            if st[-1] == '(':
                st.pop()
                st.append(2)
            else:
                temp = 0
                while st and isinstance(st[-1], int):
                    temp += st[-1]
                    st.pop()

                if not st or st[-1] != '(':
                    print("0")
                    sys.exit(0)
                st.pop()
                st.append(temp * 2)

        elif ch == ']':
            if st[-1] == '[':
                st.pop()
                st.append(3)
            else:
                temp = 0
                while st and isinstance(st[-1], int):
                    temp += st[-1]
                    st.pop()

                if not st or st[-1] != '[':
                    print("0")
                    sys.exit(0)

                st.pop()
                st.append(temp * 3)

result = 0

for v in st:
    if not isinstance(v, int):
        print("0")
        sys.exit(0)


    result += v

print(result)