#####################################
# this file is a part of Flask      #
# app project                       #
#####################################
from database_connect import connection
import gc, sys

#setting unicode char formatting
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')


class User_tools():
    def __init__(self):
        pass

    def delete(self, login):
        c, cnn = connection()
        c.execute("DELETE FROM users WHERE login=(%s)", (login,))
        cnn.commit()
        c.close()
        cnn.close()
        return None

    def add(self, name, surname, login, passwd, branch, function, permissions):
        c, cnn = connection()
        c.execute("""INSERT INTO users (name, surname, login, passwd, branch, function, uprawnienia) VALUES (%s, %s, %s, %s, $s, %s, %s)""",
                       (name, surname, login, passwd, branch, function, permissions))
        cnn.commit()
        c.close()
        cnn.close()

    def edit(self, name, surname, login, passwd, branch, function, permissions):
        c, cnn = connection()
        c.execute("""UPDATE `users` `name` = %s, `surname` = %s, `login` = %s, `passwd` = %s, `branch` = %s, `function` = %s, `uprawnienia` = %s WHERE login=(%s)""",
                  (name, surname, login, passwd, branch, function, permissions,login))
        cnn.commit()#accepting db changes
        c.close()
        cnn.close()

#verify user password
def check_passwd(login, passwd):
    c, cnn = connection()#creating cursor
    c.execute("""SELECT passwd FROM users WHERE login=(%s)""",
              (login,))#getting password from db
    try:
        temp = c.fetchall()[0][0]#request text format
        if temp != '' and temp == passwd:
            return 'Zalogowano'
        else:
            return 'Niepoprawne dane logowania!'
    except:
        return 'Niepoprawne dane logowania!'
    finally:
        c.close()
        cnn.close()
        #  gc.collect()

def show_current_users():
    pass

def send_notification(uid, data_zlecenia, data_przyjecia, tresc,
                      uzasadnienie_realizacji, opis_prac, data_prac,
                      uzasadnienie_zakupu, data_akceptacji_dyrektora,
                      data_potwierdzenia, data_zakonczenia, adresat, kom, typ):
    try:
        c, cnn = connection()
        c.execute("""INSERT INTO notifications (uid, data_zlecenia, data_przyjecia, tresc, uzasadnienie_realizacji, opis_prac, data_prac,uzasadnienie_zakupu, data_akceptacji_dyrektora, data_potwierdzenia, data_zakonczenia, adresat, kom, typ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                  (uid, data_zlecenia, data_przyjecia, tresc,uzasadnienie_realizacji, opis_prac, data_prac,uzasadnienie_zakupu, data_akceptacji_dyrektora, data_potwierdzenia, data_zakonczenia, adresat, kom, typ))
        cnn.commit()#accepting db changes
        return "Wyslane"
    except Exception as e:
        return str(e)
    finally:
        c.close()
        cnn.close()

def get_user_id(login):
    c, cnn = connection()
    c.execute("""SELECT uid FROM users WHERE login=(%s)""",
              (login,))
    try:
        temp = c.fetchall()[0][0]
        return temp
    except:
        return None
    finally:
        c.close()
        cnn.close()

def get_user_permissions(login):
    c, cnn = connection()
    c.execute("""SELECT uprawnienia FROM users WHERE login=(%s)""",
              (login,))
    try:
        temp = c.fetchall()[0][0]
        return temp
    except:
        return None
    finally:
        c.close()
        cnn.close()

def get_topics(login):
    c, cnn = connection()
    c.execute("""SELECT tresc, nid FROM notifications WHERE uid=(%s) and data_zakonczenia="" """, (get_user_id(login),))
    temp = c.fetchall()
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()

def get_all_topics(login):
    c, cnn = connection()
    c.execute("""SELECT tresc, nid FROM notifications WHERE data_zakonczenia="" """)
    temp = c.fetchall()
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()

def get_done(login):
    c, cnn = connection()
    c.execute("""SELECT tresc, nid FROM notifications WHERE uid=(%s) and data_zakonczenia > "" """, (get_user_id(login),))
    temp = c.fetchall()
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()

def get_all_done(login):
    c, cnn = connection()
    c.execute("""SELECT tresc, nid FROM notifications WHERE data_zakonczenia > "" """)
    temp = c.fetchall()
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()


def get_notification(nid):
    c, cnn = connection()
    c.execute("""SELECT * FROM notifications WHERE nid=(%s)""", (nid,))
    temp = c.fetchall()
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()

def get_branch(login):
    c, cnn = connection()
    c.execute("""SELECT branch FROM users WHERE uid=(%s)""", (get_user_id(login),))
    temp = c.fetchall()[0][0]
    try:
        return temp
    except:
        return ['blad'], ['odczytu']
    finally:
        c.close()
        cnn.close()

def savee_notification(nid, uid, data_zlecenia, data_przyjecia, tresc,
                      uzasadnienie_realizacji, opis_prac, data_prac,
                      uzasadnienie_zakupu, data_akceptacji_dyrektora,
                      data_potwierdzenia, data_zakonczenia, adresat, kom):
    try:
        c, cnn = connection()
        c.execute("""UPDATE `notifications` `uid` = %s, `data_zlecenia` = %s, `data_przyjecia` = %s, `tresc` = %s, `uzasadnienie_realizacji` = %s, `opis_prac` = %s, `data_prac` = %s, `uzasadnienie_zakupu` = %s, `data_akceptacji_dyrektora` = %s, `data_potwierdzenia` = %s, `data_zakonczenia` = %s, `adresat` = %s, `kom` = %s WHERE `notifications`.`nid` = %s""",
                  (uid, data_zlecenia, data_przyjecia, tresc,uzasadnienie_realizacji, opis_prac, data_prac,uzasadnienie_zakupu, data_akceptacji_dyrektora, data_potwierdzenia, data_zakonczenia, adresat, kom, nid))
        cnn.commit()#accepting db changes
        return "Wyslane"
    except Exception as e:
        return str(e)
    finally:
        c.close()
        cnn.close()

def save_notifiation(uid, data_zlecenia, data_przyjecia, tresc,
                      uzasadnienie_realizacji, opis_prac, data_prac,
                      uzasadnienie_zakupu, data_akceptacji_dyrektora,
                      data_potwierdzenia, data_zakonczenia, adresat, kom, typ):
    try:
        c, cnn = connection()
        c.execute("""INSERT INTO notifications (uid, data_zlecenia, data_przyjecia, tresc, uzasadnienie_realizacji, opis_prac, data_prac,uzasadnienie_zakupu, data_akceptacji_dyrektora, data_potwierdzenia, data_zakonczenia, adresat, kom, typ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                  (uid, data_zlecenia, data_przyjecia, tresc,uzasadnienie_realizacji, opis_prac, data_prac,uzasadnienie_zakupu, data_akceptacji_dyrektora, data_potwierdzenia, data_zakonczenia, adresat, kom, typ))
        cnn.commit()#accepting db changes
        return "Wyslane"
    except Exception as e:
        return str(e)
    finally:
        c.close()
        cnn.close()

def delete_nid(nid):
    try:
        c, cnn = connection()
        c.execute("""DELETE FROM notifications WHERE nid=(%s)""",(nid,))
        cnn.commit()
    except Exception as e:
        return srt(e)
    finally:
        c.close()
        cnn.close()

def get_user_id_from_nid(nid):
    c, cnn = connection()
    c.execute("""SELECT uid FROM notifications WHERE nid=(%s)""",
              (nid,))
    try:
        temp = c.fetchall()[0][0]
        return temp
    except:
        return None
    finally:
        c.close()
        cnn.close()

def get_users():
    c, cnn = connection()
    c.execute("""SELECT name, surname, login, passwd, branch, function, uprawnienia FROM users""")
    try:
        temp = c.fetchall()
        return temp
    except:
        return None
    finally:
        c.close()
        cnn.close()