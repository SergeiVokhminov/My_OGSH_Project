# Значения для выбора статуса задачи

START_STATUS = "start"
DONE_STATUS = "done"
FREE_STATUS = "free"
CLOSED_STATUS = "closed"

STATUS_CHOICES = [
    (START_STATUS, "К исполнению"),
    (DONE_STATUS, "Выполнена"),
    (FREE_STATUS, "Свободна"),
    (CLOSED_STATUS, "Отменена"),
]
