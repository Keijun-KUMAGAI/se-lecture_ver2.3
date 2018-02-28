from django.views.generic import DeleteView, UpdateView, View
from .models import Review
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from student.models import Student
from .forms import ReviewForm


# DeleteView がうまく扱えんかった・・・
class DeleteReview(View):
    model = Review
    template_name = 'review/review_delete.html'
    def get(self, request, pk):
        review = Review.objects.get(pk=pk),
        context = {
        'review':review
        }
        return render(request,self.template_name,context)
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        lecture = review.lecture
        print(lecture)
        review.delete()
        current_student = Student.objects.get_current_student(request)
        context = {
        'lecture':lecture,
        'form':ReviewForm,
        'review_list':Review.objects.filter(lecture=lecture),
        'student':current_student
        }
        return render(request,'lecture/lecture_detail.html',context)

# 後で編集するDeleteView がうまく扱えんかった・・・


# うーん・・・UpdateViewも苦手かなぁ・・・
class UpdateReview(View):
    model = Review
    fields = ('title','comment','rate_professor','rate_pass')
    template_name = 'review/review_update.html'
    success_url = reverse_lazy('lecture:detail')

    def get(self, request,pk):
        context = {
        'form':ReviewForm,
        'review':Review.objects.get(pk=pk)
        }
        return render(request,self.template_name,context)
    def post(self, request, pk):
        form = ReviewForm(request.POST or None)
        review = Review.objects.get(pk=pk)
        context = {
        'form':form,
        'review':Review.objects.get(pk=pk)
        }
        if form.is_valid():
            lecture = review.lecture
            comment = form.cleaned_data['comment']
            title = form.cleaned_data['title']
            rate_pass = form.cleaned_data['rate_pass']
            rate_professor = form.cleaned_data['rate_professor']

            review.comment = comment
            review.title = title
            review.rate_pass = rate_pass
            review.rate_professor = rate_professor
            review.save()

            current_student = Student.objects.get_current_student(request)
            context = {
            'lecture':lecture,
            'form':ReviewForm,
            'review_list':Review.objects.filter(lecture=lecture),
            'student':current_student
            }
            return render(request,'lecture/lecture_detail.html',context)
        else:
            render(request,self.template_name,context)

# endうーん・・・UpdateViewも苦手かなぁ・・・
