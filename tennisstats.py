#!/usr/bin/env python3


# dictionary is stored in the below format
# {"Playername1": [<Best-5>  <Best-3>  <Sets won> < Games Won> <Sets lost> <Games lost> ] ,
#  "Playername2": [<Best-5>  <Best-3>  <Sets won> < Games Won> <Sets lost> <Games lost> ] ,
#  ..
# }

def ProcessStats( d, winner, looser, score ) :

    if  winner  not in d.keys() :
        d [ winner ] = [ 0 for j in range(6) ]
    if  looser not in d.keys() :
        d [ looser ] = [ 0 for j in range(6) ]
    
    scorelist =  score.split(",") 
    numsets = len (scorelist)
    listwinner = d [ winner ]
    listlooser = d [ looser ]
    if numsets > 3 :
         listwinner[0] += 1       # index 0 represents number of 5 setters won
    else :
         listwinner[1] += 1       # index 1 represents number of 3 setters won 
    for singleset in scorelist :
        gamelist = singleset.split( "-" ) 
        winnergame = int( gamelist[0] )
        loosergame = int( gamelist[1] )
        listwinner[3] += winnergame # index 3 represents number of games won
        listlooser[3] += loosergame
        if winnergame > loosergame  :
            listwinner[2] += 1  #index 2 represents number of sets won
            listlooser[4] += 1  #index 4 represents number of sets lost
        else :
            listwinner[4] += 1  
            listlooser[2] += 1
       
        # index 5 represents number of games lost
        listwinner[5] +=  loosergame
        listlooser[5] +=  winnergame 

def FormPlayerStatTupleList( playerlist, d, listindex ) :
       
    if not playerlist :
        playerlist = list( d.keys() )
    tuple_list = []
    for player in playerlist :
        statlist = d[player]
        tuple_list += [ (player,statlist[listindex]) ]
    return tuple_list

def FindMaximumPlayer ( playerstat_tuples, playerlist ) :
    
    if len(playerstat_tuples) == 1 :
        return ( playerstat_tuples[0][0], None )

    if playerstat_tuples[0][1] > playerstat_tuples[1][1] :
        return ( playerstat_tuples[0][0], None )

    newplayerlist = []
    newplayerlist += [ playerstat_tuples[0][0] ]       
    (previousplayer, previousstat ) =  playerstat_tuples[0]

    for playstat in playerstat_tuples[1:] :
        if playstat[1] == previousstat :
            newplayerlist += [ playstat[0] ]
        else :
            break         
    playerlist = newplayerlist
    return ( None, playerlist )
    

def FindMinimumPlayer ( playerstat_tuples, playerlist ) :

    if len(playerstat_tuples) == 1 :
        return ( playerstat_tuples[0][0], None )

    if playerstat_tuples[0][1] < playerstat_tuples[1][1] :
        return ( playerstat_tuples[0][0], None )

    newplayerlist = []
    newplayerlist += [ playerstat_tuples[0][0] ]       
    (previousplayer, previousstat ) =  playerstat_tuples[0]

    for playstat in playerstat_tuples[1:] :
        if playstat[1] == previousstat :
            newplayerlist += [ playstat[0] ]
        else :
            break         
    playerlist = newplayerlist
    return ( None, playerlist )


def DetermineplayerwithHigherRanking( d ) :

    player = None
    listindex = 0 
    playerlist = list( d.keys() )

    
    while  listindex < 6  :
    
        playerstat_tuples = FormPlayerStatTupleList(playerlist , d, listindex)

        if listindex < 4 :
            playerstat_tuples = sorted( playerstat_tuples, 
                                        key=lambda playerstat: playerstat[1], reverse=True )
            ( player, playerlist ) = FindMaximumPlayer ( playerstat_tuples,playerlist )
        else :
            playerstat_tuples = sorted( playerstat_tuples, 
                                        key=lambda playerstat: playerstat[1], reverse=False )
            ( player, playerlist ) = FindMinimumPlayer ( playerstat_tuples,playerlist )
        if not player :
            listindex +=1 
            continue
        else :
            break
    
    return player  

        

d = {}
totaldetails = []

while( True ) :
    try :
        tennismatchdetails = input()
        if tennismatchdetails :
            totaldetails.append( tennismatchdetails )
           # retval = checktheinput(tennismatchdetails)
           # if retval != -1 :
           #     totaldetails.append( tennismatchdetails )
           # else :
           #     continue
              
        else :
           break

    except ValueError as err:
        continue

    except EOFError :
        break 
    
for n in totaldetails :
    singlematchinfo = n.split( ":" )
    winner = singlematchinfo[0]
    looser = singlematchinfo[1]
    score  = singlematchinfo[2]
                 
    ProcessStats( d, winner, looser, score )


line = ""

while ( d ) :
    
    player = DetermineplayerwithHigherRanking(d )
    if not player :
         print ("Erroneous Input")
         break   
    line +=  player 
    line = "{0} ".format(line)
    playerstats = d[player]
    
    for j in playerstats :
        stats = str(j)
        stats = "{0} ".format(stats)
        line += stats
    line = line.rstrip()
    print (line)
    line = ""
    listindex = 0 
    del ( d[player] )
    






     
    
