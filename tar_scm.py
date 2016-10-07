#!/usr/bin/env python
#
# A simple script to checkout or update a svn or git repo as source service
#
# (C) 2010 by Adrian Schroeter <adrian@suse.de>
# (C) 2014 by Jan Blunck <jblunck@infradead.org> (Python rewrite)
# (C) 2016 by Adrian Schroeter <adrian@suse.de> (OBS cpio support)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# See http://www.gnu.org/licenses/gpl-2.0.html for full license text.
import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import TarSCM
import TarSCM.tasks

def main():
    args = TarSCM.cli()
    args.parse_args()

    if os.path.basename(sys.argv[0]) == "tar":
        args.scm = "tar"
    
    if os.path.basename(sys.argv[0]) == "obs_scm":
        args.use_obs_scm = True

    if  os.path.basename(sys.argv[0]) == "snapcraft":
        args.snapcraft = True

    task_list = TarSCM.tasks()

    task_list.generate_list(args)

    task_list.process_list()

    task_list.finalize(args)


if __name__ == '__main__':
    main()
