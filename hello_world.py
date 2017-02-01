"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi


class TaskA(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget("Task.txt")

    def run(self):
        with self.output().open('w') as outputFile:
            outputFile.write('TaskA!')

class TaskB(luigi.Task):
    def requires(self):
        return TaskA()

    def output(self):
        return luigi.LocalTarget(self.input().path)

    def run(self):
        with self.input().open() as infile, self.output().open('w') as outfile:
            text = infile.read() + " TaskB!"
            outfile.write(text)



if __name__ == '__main__':
    luigi.run()
