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

'''
    }
]

def example():
    for test in tests:
        fetcher = CommentFetcher(test['language'], debug=True)
        print '\ntest for', test['language'], '\n'
        fetcher.fetch(test['content'])

if __name__ == '__main__':
    example()
