from config import SEPARATOR
from googleplay import GooglePlayApplication

def encode_item(item):
    return unicode(item).encode('utf8')

def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0

def print_header_line():
    l = [ "Title",
                "Package name",
                "Creator",
                "Super Dev",
                "Price",
                "Offer Type",
                "Version Code",
                "Size",
                "Rating",
                "Num Downloads",
             ]
    print SEPARATOR.join(l)

def print_result_line(c):
    #c.offer[0].micros/1000000.0
    #c.offer[0].currencyCode
    l = [ c.title,
                c.docid,
                c.creator,
                len(c.annotations.badgeForCreator), # Is Super Developer?
                c.offer[0].formattedAmount,
                c.offer[0].offerType,
                c.details.appDetails.versionCode,
                sizeof_fmt(c.details.appDetails.installationSize),
                "%.2f" % c.aggregateRating.starRating,
                c.details.appDetails.numDownloads]
    print SEPARATOR.join(unicode(i).encode('utf8') for i in l)

def print_result_json(c):
    appObj = GooglePlayApplication()
    appObj.title = unicode(c.title).encode('utf8')
    appObj.package = unicode(c.docid).encode('utf8')
    appObj.creator = unicode(c.creator).encode('utf8')
    appObj.developerName = unicode(c.details.appDetails.developerName).encode('utf8')
    appObj.version = unicode(c.details.appDetails.versionString).encode('utf8')
    appObj.versionCode = unicode(c.details.appDetails.versionCode).encode('utf8')
    appObj.releaseDate = unicode(c.details.appDetails.uploadDate).encode('utf8')
    appObj.downloads = unicode(c.details.appDetails.numDownloads).encode('utf8')
    appObj.size = c.details.appDetails.installationSize
    appObj.rating = unicode("%.2f" % c.aggregateRating.starRating).encode('utf8')
    appObj.ratingsCount = c.aggregateRating.ratingsCount
    appObj.kind = unicode(c.details.appDetails.appType).encode('utf8')
    appObj.primaryGenre = appObj.genres[0] if len(appObj.genres) > 0 else ""
    appObj.genres = list(map(encode_item, c.details.appDetails.appCategory))
    appObj.description = c.descriptionHtml
    appObj.recentChanges = c.details.appDetails.recentChangesHtml

    price = 0.0
    currency = "GBP"
    if hasattr(c, 'offer') and len(c.offer) > 0:
        if hasattr(c.offer[0], 'micros') and hasattr(c.offer[0], 'currencyCode'):
            price = c.offer[0].micros / 1000000.0
            currency = unicode(c.offer[0].currencyCode).encode('utf8')

    appObj.price = price
    appObj.currency = currency
    print appObj.toJSON()
