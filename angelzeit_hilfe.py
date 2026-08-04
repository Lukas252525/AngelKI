from datetime import datetime, timedelta



def zeit_bis_start(
    startzeit
):


    jetzt = datetime.now()



    stunde, minute = map(
        int,
        startzeit.split(":")
    )



    ziel = jetzt.replace(

        hour=stunde,

        minute=minute,

        second=0,

        microsecond=0

    )



    # falls Zeit schon vorbei ist:
    # nächsten Tag nehmen

    if ziel < jetzt:

        ziel += timedelta(
            days=1
        )



    unterschied = ziel - jetzt



    stunden = unterschied.seconds // 3600


    minuten = (
        unterschied.seconds % 3600
    ) // 60



    return f"{stunden}h {minuten}min"