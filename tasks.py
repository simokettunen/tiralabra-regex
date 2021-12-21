from invoke import task

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src')
    
@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage report -m')
    
@task
def pylint(ctx):
    ctx.run('pylint src')

@task
def unit_test(ctx):
    ctx.run('pytest src/tests/unit_tests')
    
@task
def integration_test(ctx):
    ctx.run('pytest src/tests/integration_tests')
    
@task
def performance_test(ctx):
    ctx.run('python3 src/performance_test.py')

@task
def start(ctx):
    ctx.run('python3 src/main.py')