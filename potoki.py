class Result(object):
    CONTINUE = 0
    DONE = 1


class UnknownResultCode(Exception):
    pass


class ReactorState(object):
    PAUSE = 0
    WORK = 1


class Reactor(object):
    state = ReactorState.PAUSE
    tasks = []

    @classmethod
    def process_task(cls):
        if not cls.tasks:
            cls.stop_reactor()

        continue_tasks = []
        for task in cls.tasks:
            for result in task:
                if result == Result.CONTINUE:
                    continue_tasks.append(task)
                    break
                elif result == Result.DONE:
                    break
                else:
                    raise UnknownResultCode(result)
        cls.tasks = continue_tasks

    @classmethod
    def start_reactor(cls):
        cls.state = ReactorState.WORK
        cls.main()

    @classmethod
    def stop_reactor(cls):
        cls.state = ReactorState.PAUSE

    @classmethod
    def main(cls):
        while cls.state == ReactorState.WORK:
            cls.process_task()


def calc_multiple(numbers):
    for number in numbers:
        print('cacl mutl', number ** 2)
        yield Result.CONTINUE
    yield Result.DONE


def calc_multiple_2(numbers):
    for number in numbers:
        print('cals2', number + 1)
        yield Result.CONTINUE
    yield Result.DONE


Reactor.tasks.append(calc_multiple([1, 2, 3]))
Reactor.tasks.append(calc_multiple_2([4, 5, 6]))
Reactor.start_reactor()