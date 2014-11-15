import email.header
    def __init__(self, filename, header):
        self.patch_author           = header['author']  if header else None
        self.patch_email            = header['email']   if header else None
        self.patch_subject          = header['subject'] if header else None

    def _read_single_patch(fp, header, oldname=None, newname=None):
        patch = PatchObject(fp.filename, header)











    header = {}

            elif line.startswith("From: "):
                author = ' '.join([data.decode(format or 'utf-8').encode('utf-8') for \
                                  data, format in email.header.decode_header(line[6:])])
                r =  re.match("\"?([^\"]*)\"? <(.*)>", author)
                if r is None: raise NotImplementedError("Failed to parse From - header.")
                header['author'] = r.group(1).strip()
                header['email']  = r.group(2).strip()
                assert fp.read() == line

            elif line.startswith("Subject: "):
                subject = line[9:].rstrip("\r\n")
                assert fp.read() == line
                while True:
                    line = fp.peek()
                    if not line.startswith(" "): break
                    subject += line.rstrip("\r\n")
                    assert fp.read() == line
                r = re.match("^\\[PATCH[^]]*\\](.*)", subject)
                if r is not None: subject = r.group(1)
                r = re.match("(.*)\\(try [0-9]+\\)$", subject)
                if r is None: r = re.match("(.*), v[0-9]+$", subject)
                if r is None: r = re.match("^[^:]+ v[0-9]+: (.*)", subject)
                if r is not None: subject = r.group(1)
                subject = subject.strip()
                if not subject.endswith("."): subject += "."
                header['subject'] = subject.strip()

                yield _read_single_patch(fp, header, tmp[2].strip(), tmp[3].strip())

                yield _read_single_patch(fp, header)

