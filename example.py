from comment_fetcher import CommentFetcher

tests = [
    {
        'language': 'python',
        'content': '''
# single line comment
def hello():
    print 'hello, world'

\'\'\'
multiple comment
simple test text string

test test test test
\'\'\'
def world():
    print 'good bye'

'''
    }, {
        'language': 'c',
        'content': '''
/*
 * this is first c program
 * multiple comment
 * multiple comment
 */
#include <stdio.h>

// hello, world!
int main() {
    return printf("hello, world!");
}

// test auto merge multiline comments
// second line
// third line
// end comment

// single line
int add(int a, int b) {
    return a + b;
}
'''
    }
]

def example():
    for test in tests:
        fetcher = CommentFetcher(test['language'], debug=True)
        print '\ntest for', test['language'], '\n'
        comments = fetcher.fetch(test['content'])
        print '\n result:\n'
        for cmt in comments:
            print cmt
            print '\n'

if __name__ == '__main__':
    example()
