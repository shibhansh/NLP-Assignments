langname = english
langcode = en

analyzer_transducer = $(langcode)-analysis.hfst.ol
generator_transducer = $(langcode)-generation.hfst.ol
prefix = /usr/local
transducerpath = $(prefix)/share/hfst/en
binarypath = $(prefix)/bin
analyzer_script = $(binarypath)/${langname}-analyze.sh
generator_script = $(binarypath)/${langname}-generate.sh

install:
	install -m 0775 -d $(transducerpath)
	install -m 0664 $(analyzer_transducer) --target-directory=$(transducerpath)
	install -m 0664 $(generator_transducer) --target-directory=$(transducerpath)
	sed -e s,BINPATH,$(binarypath),g -e s,TRPATH,$(transducerpath),g \
		< ${langname}-analyze.sh > $(binarypath)/${langname}-analyze.sh
	sed -e s,BINPATH,$(binarypath),g -e s,TRPATH,$(transducerpath),g \
		< ${langname}-generate.sh > $(binarypath)/${langname}-generate.sh
	chmod 0755 $(analyzer_script)
	chmod 0755 $(generator_script)

uninstall:
	rm -f $(transducerpath)/$(analyzer_transducer)
	rm -f $(transducerpath)/$(generator_transducer)
	rmdir --ignore-fail-on-non-empty $(transducerpath)
	rm -f $(analyzer_script)
	rm -f $(generator_script)
