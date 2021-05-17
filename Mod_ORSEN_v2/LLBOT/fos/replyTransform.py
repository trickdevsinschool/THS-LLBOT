from .fosChecker import check


def call(reply):
    reply= reply.replace('.','')
    slicedreply= reply.split()
    keyword= slicedreply[-1]
    fos,sori= check(keyword)
    if sori=="S":
        finalreply= reply +" " + fos
    elif sori=="I":
        finalreply= reply.replace(keyword,fos)
    else:
        finalreply=reply

    return finalreply


    



