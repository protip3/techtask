s ="123;122.5;0.5;0.0;123.5"

def task3(st):
    return max(list(map(float,st.split(';'))))

print(task3(s))