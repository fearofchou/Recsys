import subprocess
import sys
def convert_Transpose(BS_file):
    co = '/home/fearofchou/Tools/libfm-1.40.src/bin/convert'
    fi = ' --ifile ' + BS_file
    fox = ' --ofilex ' + BS_file + '.x'
    foy = ' --ofiley ' + BS_file + '.y'
    subprocess.call(co + fi + fox + foy,shell = True)

    tr = '/home/fearofchou/Tools/libfm-1.40.src/bin/transpose'
    fi = ' --ifile ' + BS_file + '.x'
    fo = ' --ofile ' + BS_file + '.xt'
    subprocess.call(tr + fi + fo,shell = True)



if __name__ == '__main__':
    convert_Transpose(sys.argv[1])
