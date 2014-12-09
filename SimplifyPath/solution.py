class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        tmp = [ t for t in path.split("/") if len(t) >0 ]

        q = list()

        for dir_name in tmp:
            if dir_name == ".":
                continue
            elif dir_name == "..":
                if len(q) >0:
                    q.pop()
            else:
                q.append(dir_name)

        return "/%s" % ("/".join(q))

if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/home/")
    print s.simplifyPath("/a/./b/../../c/")
    print s.simplifyPath("/..")
    print s.simplifyPath("/abc/...")
