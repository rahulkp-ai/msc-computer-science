def naive_bayes_classify(words, spam_probs, ham_probs, p_spam=0.5, p_ham=0.5):
    spam_score  = p_spam
    ham_score   = p_ham
    for word in words:
        spam_score  *= spam_probs.get(word, 0.5)
        ham_score   *= ham_probs.get(word, 0.5)
    return "SPAM"   if spam_score > ham_score   else "NOT SPAM"

spam_probs  = {"free": 0.8, "meeting": 0.1}
ham_probs   = {"free": 0.1, "meeting": 0.7}

print(naive_bayes_classify(["free","free"], spam_probs,ham_probs))
print(naive_bayes_classify(["meeting"], spam_probs, ham_probs))