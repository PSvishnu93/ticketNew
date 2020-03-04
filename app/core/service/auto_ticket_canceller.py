import time
from datetime import datetime
from datetime import timedelta
import pymysql


class AutoTicketCanceller:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='celluloid',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    expiry_time = 3
    sleep_time = 1

    def cancel_tickets(self):
        print("Job activated")
        while True:
            now = datetime.now()
            min_time = now - timedelta(minutes=3)
            reservation_query = f"""Select id from celluloid.user_reservation
                                where status_id=1 and
                                reserved_on<='{min_time}'"""
            reservation_update_query = f"""update user_reservation set
                                           status_id=3 where status_id=1  and
                                           reserved_on<='{min_time}'"""
            ticket_query = f"""select ticket_id from seat_reservation where
                               user_reservation_id in ({reservation_query})"""
            ticket_update_query = f"""update ticket set ticket_status=1
                                      where id in ({ticket_query})"""
            with AutoTicketCanceller.connection.cursor() as cur:
                cur.execute(ticket_update_query)
                cur.execute(reservation_update_query)
            AutoTicketCanceller.connection.commit()
            time.sleep(60)
