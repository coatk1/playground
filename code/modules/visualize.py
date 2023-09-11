# Third-party Libraries
import sklearn.metrics as skm
import matplotlib.pyplot as plt


def display_model_report(y_test: list, y_pred, model="model"):

    # NOTE:
    # precision = TP / (TP + FP). See vertical axis on confusion matrix, add total predicted. Correctness of positive prediction.
    # recall = TP / (TP + FN). See horizontal axis on confusion matrix, add total predicted. Ground truth/ true positive rate.
    # accuracy = (TP + TN) / (TP + TN + FP + FN). Correct predictions/ Total predictions.
    # Higher F-score = more accurate predictions.

    print("Metrics for {} model:\n".format(model), skm.classification_report(y_test, y_pred))

    return None


def display_model_scores(y_test: list, y_pred, average: str = None, model="model"):

    print("Accuracy score for {} model: {:.2f}%".format(model, skm.accuracy_score(y_test, y_pred) * 100))
    print("Precision score for {} model: {:.2f}%".format(model, skm.precision_score(y_test, y_pred, average=average) * 100))
    print("Recall score for {} model: {:.2f}%".format(model, skm.recall_score(y_test, y_pred, average=average) * 100))
    print("F1 score for {} model: {:.2f}%".format(model, skm.f1_score(y_test, y_pred, average=average) * 100))

    return None


def display_multiclass_model_matrix(y_test: list, y_pred, model, save=False):

    c_matrix = skm.confusion_matrix(y_test, y_pred, labels=model.classes_, normalize="pred")

    # Get the TN, FP, FN, TP values.
    # c_matrix.ravel()

    disp = skm.ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=model.classes_)
    disp.plot()

    plt.xticks(rotation=45, ha="right")
    if save:
        plt.savefig("multiclass_model.jpg")
    else:
        plt.show()

    return None


def display_binary_model_matrix(y_test: list, y_pred, model, topic, save=False):

    c_matrix = skm.confusion_matrix(y_test, y_pred, labels=model.classes_, normalize="pred")

    # Get the TN, FP, FN, TP values.
    # c_matrix.ravel()

    disp = skm.ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=model.classes_)
    disp.plot()

    plt.xticks(rotation=45, ha="right")
    if save:
        plt.savefig("{}_binary_model.jpg".format(topic))
    else:
        plt.show()

    return None
