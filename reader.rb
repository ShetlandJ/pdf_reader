require 'origami'
include Origami

pdf = PDF.read "home_report.pdf"

pdf.each_page do |page|
  p page.class
end
