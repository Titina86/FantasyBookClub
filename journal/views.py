from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from journal.forms import ReadingJournalForm
from journal.models import ReadingJournal


class ReadingJournalCreateView(LoginRequiredMixin, CreateView):
    model = ReadingJournal
    form_class = ReadingJournalForm
    template_name = 'journal/journal-create.html'
    success_url = reverse_lazy('profile-details')  # Redirect after successful form submission

    def form_valid(self, form):
        # Associate the new journal entry with the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)
