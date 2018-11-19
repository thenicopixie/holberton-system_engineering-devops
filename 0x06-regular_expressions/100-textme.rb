#!/usr/bin/env ruby
str1 = ARGV[0].scan(/(?<=from:).*?(?=\])/)
str2 = ARGV[0].scan(/(?<=to:).*?(?=\])/)
str3 = ARGV[0].scan(/(?<=flags:).*?(?=\])/)
puts [str1, str2, str3].join(',')

