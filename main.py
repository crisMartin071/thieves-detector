import cv2
import face_recognition as fr
import os
import numpy
import time

def codify_pictures(pictures):
    codify_list = []

    for picture in pictures:
        clear_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        codify_list.append(fr.face_encodings(clear_picture)[0])

    return codify_list

def show_limits_partameters(picture, status, best_result):
    result = fr.face_locations(picture)

    if result:
        face = result[0]

        if status == "Dangerous":
            cv2.rectangle(picture, (int(face[3]), int(face[0])), (int(face[2]), int(face[1])), (0, 0, 255), 2)
            
            similar_picture = fr.face_locations(best_result)[0]
            cv2.rectangle(best_result, (int(similar_picture[3]), int(similar_picture[0])), (int(similar_picture[2]), int(similar_picture[1])), (0, 0, 255), 2)
            cv2.imshow("Similar face", best_result)

        elif status == "Caution":
            cv2.rectangle(picture, (int(face[3]), int(face[0])), (int(face[2]), int(face[1])), (0, 165, 255), 2)

            similar_picture = fr.face_locations(best_result)[0]
            cv2.rectangle(best_result, (int(similar_picture[3]), int(similar_picture[0])), (int(similar_picture[2]), int(similar_picture[1])), (0, 165, 255), 2)
            cv2.imshow("Similar face", best_result)

        else:
            cv2.rectangle(picture, (int(face[3]), int(face[0])), (int(face[2]), int(face[1])), (0, 255, 0), 2)

        cv2.imshow("Face", picture)
    else:
        print("No se pudo tomar tu cara")

def cap_picture():
    print("Muestrate en la camara")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    for i in range(0, 5, -1):
        print("Se va a hacer la foto en "+ i + " segundos")
        time.sleep(1)
        cap.read()

    success, picture = cap.read()
    cap.release()

    if success:
        if fr.face_encodings(picture):
            return picture, fr.face_encodings(picture)[0]
    
    print("No se reconocio ninguna cara")
    return False, None


def compare_pictures(face_list, picture_list):
    picture, cap = cap_picture()

    if cap is not None: 
        status = 0
        matches = fr.compare_faces(face_list, cap, 0.4)
        distances = fr.face_distance(face_list, cap)

        if True not in matches:
            min_value = numpy.min(distances)

            if min_value > 0.4 and min_value < 0.7:
                status = "Caution"
            else:
                status = "Innocent"
        else:
            status = "Dangerous"

        show_limits_partameters(picture, status, picture_list[numpy.argmin(distances)])

    cv2.waitKey(0)

route = "Thieves"
thief_list = os.listdir(route)
pictures = []
thief_names = []

for name in thief_list:
    pictures.append(cv2.imread(f"{route}/{name}"))
    thief_names.append(name.split(".")[0])

compare_pictures(codify_pictures(pictures), pictures)
