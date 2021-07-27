from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
from reviews.utils import initialled_name

# # Register your models here.


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ["title", "isbn13"]
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", "isbn", "publisher__name")


# class BookAdmin(admin.ModelAdmin):
#     list_display = ("title", "isbn13")

#     def isbn13(self, obj):
#         """'9780316769174' => '978-0-31-676917-4'"""
#         return "{}-{}-{}-{}-{}".format(
#             obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]
#         )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content", "rating")}),
    )


@admin.register(BookContributor)
class BookContributorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
    )
