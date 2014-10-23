# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

PIPELINE_COMPILERS = (
    'activeseed.lib.pylesswrap.pipeline_compiler.PyLessWrapCompiler',
)

PIPELINE_CSS = {
    'test': {
        'source_filenames': (
            'activeseed/bootstrap/bootstrap.less',
        ),
        'output_filename': 'css/bootstrap.css',
    },
}
