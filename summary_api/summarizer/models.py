from django.db import models

class Summary(models.Model):
    """
    Model to store the original text, generated summary, and bullet points.
    """
    original_text = models.TextField()
    summary = models.TextField(null=True, blank=True)
    bullet_points = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary {self.id} - Created on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
