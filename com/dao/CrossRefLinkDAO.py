#coding=utf-8
from com.dao import *

class CrossRefLinkDAO(DAO):
	table='cross_ref_link_en'

	def __init__(self):
		DAO.__init__(self)

	def deleteBySrcId(self,srcId):
		if srcId:
			try:
				self.cursor_stg.execute('delete from %s where src_article_id=%s' % (CrossRefLinkDAO.table,srcId))
				self.conn_stg.commit()
			except Exception,e:
				self.log.error(e)

	def deleteByDesId(self,desId):
		if desId:
			try:
				self.cursor_stg.execute('delete from %s where src_article_id=%s' % (CrossRefLinkDAO.table,desId))
				self.conn_stg.commit()
			except Exception,e:
				self.log.error(e)
		
			
	def insert(self,crossRefLink):
		try:
			self.cursor_stg.execute("REPLACE INTO "+CrossRefLinkDAO.table+"(src_article_id,keyword_id,des_article_id,des_item_id,des_attachment_id) VALUES(%s,%s,%s,%s,%s)" % (crossRefLink.srcId,crossRefLink.keywordId,crossRefLink.desId,crossRefLink.desItemId,crossAttachId))
			self.conn.commit()
		except Exception,e:
			self.log.error(e) 
			self.log.error("Error occured in insert() of CrossRefLinkDAO.py")

	def add(self,crossRefLink):
		try:
			self.cursor_stg.execute("replace into "+CrossRefLinkDAO.table+"(src_article_id,keyword_id,des_article_id,des_item_id,des_attachment_id,src_content_type,src_origin_id,src_provider_id,src_isenglish,des_content_type,des_origin_id,des_provider_id,des_isenglish) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % crossRefLink.toTuple())
		except Exception,e:
			self.log.error(e)
			self.log.error("Error occured in add() of CrossRefLinkDAO")
	

	def getBySrcId(self,srcId):
		"get link between article of src Id"
		pass

	def getByDesId(self,desId):
		pass

	def getByDesSrcId(self,desId,srcId):
		pass
	
	def getRelatedArticleId(self,id,contentType):
		try:
			sql=("SELECT des_article_id AS articleId,des_content_type as content_type FROM "+CrossRefLinkDAO.table+" WHERE src_article_id=%s and src_content_type='%s' UNION SELECT src_article_id AS articleId,src_content_type as content_type FROM "+CrossRefLinkDAO.table+" WHERE des_article_id=%s and des_content_type='%s'; ") %(id,contentType,id,contentType)
			self.cursor_stg.execute(sql)
			return self.cursor_stg.fetchall()
		except Exception,e:
			self.log.error(e)
			self.log.error(sql)

	def collectRelativeStastics(self,desOriginId,desProviderId,desIsEnglish,desContentType):
		try:
	    		sql="select des_item_id,src_content_type,count(*) from "+CrossRefLinkDAO.table+" where des_origin_id='%s' and des_provider_id=%s and des_isEnglish='%s' and des_content_type='%s' and des_item_id <>0 group by src_content_type,des_item_id order by des_item_id asc;" %(desOriginId,desProviderId,desIsEnglish,desContentType)
	    		self.cursor_stg.execute(sql)
	    		return self.cursor_stg.fetchall()
		except Exception,e:
	    		self.log.error(e)
			self.log.error("collectRelativeStatistics() in CrossRefLinkDAO.py")
