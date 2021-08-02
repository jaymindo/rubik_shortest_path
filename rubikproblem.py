testData = (
    "B", "B", "O", "B",
    "O", "G", "G", "W",
    "W", "W", "O", "R",
    "R", "R", "Y", "B",
    "Y", "Y", "G", "O",
    "R", "Y", "W", "G")

#6 functions to apply the move 
def L(cube):
    return (cube[14],  cube[1], cube[2], cube[13],
            cube[0],  cube[5], cube[6], cube[3],
            cube[8],  cube[9], cube[10], cube[11],
            cube[12],  cube[23], cube[20], cube[15],
            cube[19],  cube[16], cube[17], cube[18],
            cube[4],  cube[21], cube[22], cube[7]
            )


def Li(cube):
    return (cube[4],  cube[1], cube[2], cube[7],
            cube[20],  cube[5], cube[6], cube[23],
            cube[8],  cube[9], cube[10], cube[11],
            cube[12],  cube[3], cube[0], cube[15],
            cube[17],  cube[18], cube[19], cube[16],
            cube[14],  cube[21], cube[22], cube[13]
            )


def B(cube):
    return (cube[9],  cube[10], cube[2], cube[3],
            cube[4],  cube[5], cube[6], cube[7],
            cube[8],  cube[22], cube[23], cube[11],
            cube[15],  cube[12], cube[13], cube[14],
            cube[1],  cube[17], cube[18], cube[0],
            cube[20],  cube[21], cube[19], cube[16]
            )


def Bi(cube):
    return(cube[19],  cube[16], cube[2], cube[3],
           cube[4],  cube[5], cube[6], cube[7],
           cube[8],  cube[0], cube[1], cube[11],
           cube[13],  cube[14], cube[15], cube[12],
           cube[23],  cube[17], cube[18], cube[22],
           cube[20],  cube[21], cube[9], cube[10]
           )


def D(cube):
    return(cube[0],  cube[1], cube[2], cube[3],
           cube[4],  cube[5], cube[10], cube[11],
           cube[8],  cube[9], cube[14], cube[15],
           cube[12],  cube[13], cube[18], cube[19],
           cube[16],  cube[17], cube[6], cube[7],
           cube[21],  cube[22], cube[23], cube[20]
           )


def Di(cube):
    return(cube[0],  cube[1], cube[2], cube[3],
           cube[4],  cube[5], cube[18], cube[19],
           cube[8],  cube[9], cube[6], cube[7],
           cube[12],  cube[13], cube[10], cube[11],
           cube[16],  cube[17], cube[14], cube[15],
           cube[23],  cube[20], cube[22], cube[21]
           )


# From graphys.py obtained from CAB203 Blackboard
moves = {L, Li, B, Bi, D, Di}

# From graphys.py obtained from CAB203 Blackboard


def N(v):
    return {move(v) for move in moves}


def checkSolved(tuple):
    solved_cube = False
    if(
        tuple[0] == tuple[1] == tuple[2] == tuple[3] and
        tuple[4] == tuple[5] == tuple[6] == tuple[7] and
        tuple[8] == tuple[9] == tuple[10] == tuple[11] and
        tuple[12] == tuple[13] == tuple[14] == tuple[15] and
        tuple[16] == tuple[17] == tuple[18] == tuple[19] and
        tuple[20] == tuple[21] == tuple[22] == tuple[23]
    ):
        solved_cube = True
    return solved_cube

# Modified from graphys.py obtained from CAB203 Blackboard
def distanceClassesP(u):
    print("processing...")
    D = [{u}]  # D[0] = D_0 = {u}
    if(checkSolved(u)):
        return D
    return distanceClassesPR(D, u)

# Modified from graphys.py obtained from CAB203 Blackboard
# we now stop when we find the target vertex rather then
# if we run out of vertices or if graph is disconnected.
# Graph is known to be connected so we will always get to target.
def distanceClassesPR(D, u):
    v_temp = set()
    for d in D:
        for i in d:
            v_temp = v_temp | N(i)
    Dnew = D + [v_temp]  # D_{j} = N_{V_j}(D_{j-1})
    for d in Dnew:
        for i in d:
            if checkSolved(i) == True:
                return Dnew
    return distanceClassesPR(Dnew, u)


def solution(instance):
    D = distanceClassesP(instance)
    return D


def print_solution(solution):
    print("The shortest number of moves is:", len(solution)-1)


print_solution(solution(testData))
