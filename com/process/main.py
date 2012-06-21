from com.process.KeywordHyperlinkProcess import *
from com.process.VersionHyperlinkProcess import *
from com.process.AbbreviationHyperlinkProcess import *


if __name__=='__main__':
	khp=KeywordHyperlinkProcess.KeywordHyperlinkProcess()
	vhp=VersionHyperlinkProcess.VersionHyperlinkProcess()
	ahp=AbbreviationHyperlinkProcess.AbbreviationHyperlinkProcess()
	
	i=1
	for queueItem in self.queueDao.getByContentType(Article.CONTENT_TYPE_LAW):
		if i>1:break
		i+=1
		khp.begin(queueItem)
		article=khp.getArticle(queueItem)
		article=khp.process(article)
		article=vhp.process(article)
		article=ahp.process(article)
		khp.updateArticle(article)
		khp.end(queueItem)
