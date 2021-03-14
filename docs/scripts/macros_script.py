import math

def define_env(env):
    "Hook function"

    pi = math.pi

    @env.macro
    def pi_string(dp=2):
        fmt = '{:.' + str(dp) + 'f}'
        return fmt.format(pi)
