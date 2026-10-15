from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import HabitSerializer, CheckInSerializer
from django.shortcuts import get_object_or_404
from habits.models import Habit
from checkins.models import CheckIn


'''define the rules of seeing habits or creating one'''


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def habit_list_create(request):
    if request.method == 'GET':
        habits = request.user.habits.all().order_by('-created_at')

        serializer = HabitSerializer(habits, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    serializer = HabitSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


'''define the rules of edit a habit'''


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def habit_detail(request, pk):
    habit = get_object_or_404(
        Habit,
        pk=pk,
        user=request.user
    )

    if request.method == 'GET':
        serializer = HabitSerializer(habit)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    if request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'

        serializer = HabitSerializer(
            habit,
            data=request.data,
            partial=partial
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        habit.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


'''define the rules of seeing checkins of a habit or edit one'''


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def checkin_list_create(request):
    if request.method == 'GET':
        checkins = CheckIn.objects.filter(
            habit__user=request.user
        ).order_by('-date')

        serializer = CheckInSerializer(
            checkins,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    serializer = CheckInSerializer(data=request.data)

    if serializer.is_valid():
        habit = serializer.validated_data['habit']

        if habit.user != request.user:
            return Response(
                {
                    'habit': 'این عادت متعلق به کاربر واردشده نیست.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
