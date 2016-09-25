#!usr/bin/env python

def main():
    input = raw_input().split(' ')
    output = []

    for word in input:
        if word:
            output.append(word[0].upper() + word[1:].lower())
        else:
            output.append('')

    print ' '.join(output)

if __name__ == '__main__':
    main()